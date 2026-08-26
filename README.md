# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 410
- HTTP: 105 alive / 69 gold
- HTTPS: 57 alive / 17 gold
- SOCKS4: 163 alive / 159 gold
- SOCKS5: 182 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38948
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
