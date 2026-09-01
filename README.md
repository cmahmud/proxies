# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 424
- HTTP: 97 alive / 69 gold
- HTTPS: 66 alive / 26 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 181 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47065
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
