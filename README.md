# SyndProxy validated proxy pool

## Current pool

- Alive now: 614
- Gold now: 458
- HTTP: 125 alive / 88 gold
- HTTPS: 123 alive / 31 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 193 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46730
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
