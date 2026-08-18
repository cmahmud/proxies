# SyndProxy private pool

## Current pool

- Alive now: 864
- Gold now: 265
- HTTP: 247 alive / 32 gold
- HTTPS: 200 alive / 5 gold
- SOCKS4: 206 alive / 119 gold
- SOCKS5: 211 alive / 109 gold

## Historical pool

- Discovered: 99124
- Ever alive: 11875
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
