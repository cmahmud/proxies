# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 345
- HTTP: 125 alive / 40 gold
- HTTPS: 53 alive / 10 gold
- SOCKS4: 166 alive / 152 gold
- SOCKS5: 199 alive / 143 gold

## Historical pool

- Discovered: 171565
- Ever alive: 32882
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
