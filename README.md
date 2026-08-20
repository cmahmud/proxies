# SyndProxy private pool

## Current pool

- Alive now: 1692
- Gold now: 650
- HTTP: 643 alive / 210 gold
- HTTPS: 472 alive / 117 gold
- SOCKS4: 242 alive / 157 gold
- SOCKS5: 335 alive / 166 gold

## Historical pool

- Discovered: 141215
- Ever alive: 23929
- Ever gold: 964

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
