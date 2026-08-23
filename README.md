# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 214
- HTTP: 155 alive / 51 gold
- HTTPS: 141 alive / 11 gold
- SOCKS4: 101 alive / 68 gold
- SOCKS5: 157 alive / 84 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32682
- Ever gold: 1200

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
