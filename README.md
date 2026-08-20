# SyndProxy private pool

## Current pool

- Alive now: 828
- Gold now: 392
- HTTP: 259 alive / 86 gold
- HTTPS: 164 alive / 20 gold
- SOCKS4: 201 alive / 144 gold
- SOCKS5: 204 alive / 142 gold

## Historical pool

- Discovered: 144843
- Ever alive: 25323
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
