# SyndProxy validated proxy pool

## Current pool

- Alive now: 576
- Gold now: 443
- HTTP: 137 alive / 86 gold
- HTTPS: 72 alive / 35 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 196 alive / 164 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44124
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
