# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 453
- HTTP: 113 alive / 88 gold
- HTTPS: 72 alive / 32 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 193 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45569
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
