# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 398
- HTTP: 149 alive / 66 gold
- HTTPS: 45 alive / 15 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 188 alive / 160 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33283
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
