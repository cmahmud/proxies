# SyndProxy validated proxy pool

## Current pool

- Alive now: 706
- Gold now: 458
- HTTP: 167 alive / 87 gold
- HTTPS: 121 alive / 37 gold
- SOCKS4: 184 alive / 161 gold
- SOCKS5: 234 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45330
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
