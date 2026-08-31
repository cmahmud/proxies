# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 451
- HTTP: 154 alive / 89 gold
- HTTPS: 93 alive / 28 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 229 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45346
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
