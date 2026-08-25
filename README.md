# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 425
- HTTP: 104 alive / 69 gold
- HTTPS: 96 alive / 22 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 193 alive / 173 gold

## Historical pool

- Discovered: 183874
- Ever alive: 35730
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
