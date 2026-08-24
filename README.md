# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 380
- HTTP: 103 alive / 55 gold
- HTTPS: 37 alive / 8 gold
- SOCKS4: 165 alive / 154 gold
- SOCKS5: 189 alive / 163 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33435
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
