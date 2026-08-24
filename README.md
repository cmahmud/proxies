# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 389
- HTTP: 121 alive / 60 gold
- HTTPS: 29 alive / 9 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 196 alive / 164 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33435
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
