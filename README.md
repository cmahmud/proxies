# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 380
- HTTP: 93 alive / 52 gold
- HTTPS: 40 alive / 11 gold
- SOCKS4: 171 alive / 153 gold
- SOCKS5: 188 alive / 164 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33431
- Ever gold: 1237

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
