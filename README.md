# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 362
- HTTP: 88 alive / 36 gold
- HTTPS: 43 alive / 11 gold
- SOCKS4: 169 alive / 155 gold
- SOCKS5: 178 alive / 160 gold

## Historical pool

- Discovered: 171600
- Ever alive: 32940
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
