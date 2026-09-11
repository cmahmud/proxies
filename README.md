# SyndProxy validated proxy pool

## Current pool

- Alive now: 468
- Gold now: 371
- HTTP: 91 alive / 68 gold
- HTTPS: 46 alive / 22 gold
- SOCKS4: 142 alive / 112 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48725
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
