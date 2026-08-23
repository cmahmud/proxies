# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 350
- HTTP: 117 alive / 40 gold
- HTTPS: 51 alive / 9 gold
- SOCKS4: 166 alive / 152 gold
- SOCKS5: 178 alive / 149 gold

## Historical pool

- Discovered: 171048
- Ever alive: 32851
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
