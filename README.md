# SyndProxy validated proxy pool

## Current pool

- Alive now: 722
- Gold now: 455
- HTTP: 174 alive / 86 gold
- HTTPS: 129 alive / 34 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 241 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45337
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
