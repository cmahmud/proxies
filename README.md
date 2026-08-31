# SyndProxy validated proxy pool

## Current pool

- Alive now: 674
- Gold now: 452
- HTTP: 164 alive / 88 gold
- HTTPS: 95 alive / 28 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 237 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45345
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
