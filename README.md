# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 362
- HTTP: 115 alive / 36 gold
- HTTPS: 48 alive / 10 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 191 alive / 157 gold

## Historical pool

- Discovered: 171584
- Ever alive: 32928
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
