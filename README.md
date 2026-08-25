# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 406
- HTTP: 101 alive / 64 gold
- HTTPS: 90 alive / 19 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35435
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
