# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 390
- HTTP: 134 alive / 52 gold
- HTTPS: 45 alive / 13 gold
- SOCKS4: 175 alive / 156 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33629
- Ever gold: 1244

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
