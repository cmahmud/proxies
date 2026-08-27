# SyndProxy validated proxy pool

## Current pool

- Alive now: 650
- Gold now: 402
- HTTP: 97 alive / 59 gold
- HTTPS: 182 alive / 18 gold
- SOCKS4: 176 alive / 157 gold
- SOCKS5: 195 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40653
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
