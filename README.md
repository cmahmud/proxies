# SyndProxy private pool

## Current pool

- Alive now: 890
- Gold now: 401
- HTTP: 272 alive / 90 gold
- HTTPS: 172 alive / 26 gold
- SOCKS4: 221 alive / 150 gold
- SOCKS5: 225 alive / 135 gold

## Historical pool

- Discovered: 165824
- Ever alive: 32342
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
