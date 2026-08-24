# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 390
- HTTP: 109 alive / 63 gold
- HTTPS: 40 alive / 11 gold
- SOCKS4: 163 alive / 155 gold
- SOCKS5: 182 alive / 161 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33436
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
