# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 407
- HTTP: 110 alive / 60 gold
- HTTPS: 170 alive / 17 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 195 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40738
- Ever gold: 1311

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
