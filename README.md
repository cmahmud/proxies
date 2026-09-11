# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 399
- HTTP: 93 alive / 65 gold
- HTTPS: 34 alive / 18 gold
- SOCKS4: 161 alive / 143 gold
- SOCKS5: 192 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48782
- Ever gold: 1566

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
