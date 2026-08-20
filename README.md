# SyndProxy private pool

## Current pool

- Alive now: 724
- Gold now: 372
- HTTP: 178 alive / 58 gold
- HTTPS: 119 alive / 17 gold
- SOCKS4: 202 alive / 147 gold
- SOCKS5: 225 alive / 150 gold

## Historical pool

- Discovered: 147647
- Ever alive: 25863
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
