# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 462
- HTTP: 132 alive / 99 gold
- HTTPS: 60 alive / 32 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 188 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49332
- Ever gold: 1578

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
