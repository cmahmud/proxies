# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 439
- HTTP: 111 alive / 87 gold
- HTTPS: 57 alive / 31 gold
- SOCKS4: 174 alive / 155 gold
- SOCKS5: 182 alive / 166 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49432
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
