# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 392
- HTTP: 85 alive / 61 gold
- HTTPS: 73 alive / 18 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 164 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37535
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
