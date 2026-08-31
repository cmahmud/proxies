# SyndProxy validated proxy pool

## Current pool

- Alive now: 692
- Gold now: 457
- HTTP: 164 alive / 86 gold
- HTTPS: 117 alive / 35 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 233 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45330
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
