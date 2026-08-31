# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 455
- HTTP: 125 alive / 85 gold
- HTTPS: 105 alive / 35 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 187 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45625
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
