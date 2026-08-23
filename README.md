# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 338
- HTTP: 117 alive / 39 gold
- HTTPS: 45 alive / 10 gold
- SOCKS4: 166 alive / 149 gold
- SOCKS5: 194 alive / 140 gold

## Historical pool

- Discovered: 171565
- Ever alive: 32883
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
