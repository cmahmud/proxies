# SyndProxy private pool

## Current pool

- Alive now: 950
- Gold now: 404
- HTTP: 275 alive / 92 gold
- HTTPS: 203 alive / 18 gold
- SOCKS4: 225 alive / 150 gold
- SOCKS5: 247 alive / 144 gold

## Historical pool

- Discovered: 155695
- Ever alive: 29275
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
