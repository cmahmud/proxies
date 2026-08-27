# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 413
- HTTP: 96 alive / 67 gold
- HTTPS: 177 alive / 18 gold
- SOCKS4: 181 alive / 159 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40698
- Ever gold: 1311

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
