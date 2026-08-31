# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 450
- HTTP: 118 alive / 87 gold
- HTTPS: 66 alive / 31 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 202 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45566
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
