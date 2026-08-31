# SyndProxy validated proxy pool

## Current pool

- Alive now: 702
- Gold now: 460
- HTTP: 164 alive / 90 gold
- HTTPS: 117 alive / 34 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 241 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45335
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
