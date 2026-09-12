# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 463
- HTTP: 130 alive / 96 gold
- HTTPS: 54 alive / 32 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 189 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49408
- Ever gold: 1580

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
