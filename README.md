# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 419
- HTTP: 115 alive / 74 gold
- HTTPS: 177 alive / 21 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40567
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
