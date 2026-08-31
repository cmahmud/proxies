# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 445
- HTTP: 145 alive / 78 gold
- HTTPS: 106 alive / 34 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 203 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45373
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
