# SyndProxy private pool

## Current pool

- Alive now: 732
- Gold now: 378
- HTTP: 194 alive / 60 gold
- HTTPS: 93 alive / 15 gold
- SOCKS4: 226 alive / 148 gold
- SOCKS5: 219 alive / 155 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25790
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
