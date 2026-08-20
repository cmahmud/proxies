# SyndProxy private pool

## Current pool

- Alive now: 1667
- Gold now: 653
- HTTP: 626 alive / 211 gold
- HTTPS: 482 alive / 116 gold
- SOCKS4: 236 alive / 159 gold
- SOCKS5: 323 alive / 167 gold

## Historical pool

- Discovered: 141215
- Ever alive: 23929
- Ever gold: 964

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
