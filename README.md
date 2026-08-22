# SyndProxy private pool

## Current pool

- Alive now: 913
- Gold now: 426
- HTTP: 274 alive / 85 gold
- HTTPS: 175 alive / 32 gold
- SOCKS4: 208 alive / 144 gold
- SOCKS5: 256 alive / 165 gold

## Historical pool

- Discovered: 162748
- Ever alive: 31512
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
