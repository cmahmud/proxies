# SyndProxy validated proxy pool

## Current pool

- Alive now: 715
- Gold now: 458
- HTTP: 170 alive / 89 gold
- HTTPS: 121 alive / 35 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 243 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45336
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
