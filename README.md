# SyndProxy validated proxy pool

## Current pool

- Alive now: 609
- Gold now: 454
- HTTP: 127 alive / 85 gold
- HTTPS: 118 alive / 35 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45620
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
