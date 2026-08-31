# SyndProxy validated proxy pool

## Current pool

- Alive now: 712
- Gold now: 457
- HTTP: 171 alive / 87 gold
- HTTPS: 121 alive / 35 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 240 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45336
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
