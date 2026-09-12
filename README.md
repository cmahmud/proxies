# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 467
- HTTP: 133 alive / 95 gold
- HTTPS: 46 alive / 32 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 191 alive / 177 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49414
- Ever gold: 1580

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
