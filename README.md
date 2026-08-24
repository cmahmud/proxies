# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 391
- HTTP: 120 alive / 55 gold
- HTTPS: 72 alive / 14 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 190 alive / 163 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33380
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
