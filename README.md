# SyndProxy validated proxy pool

## Current pool

- Alive now: 706
- Gold now: 458
- HTTP: 170 alive / 87 gold
- HTTPS: 121 alive / 36 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 234 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45331
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
