# SyndProxy private pool

## Current pool

- Alive now: 1147
- Gold now: 551
- HTTP: 386 alive / 171 gold
- HTTPS: 316 alive / 83 gold
- SOCKS4: 224 alive / 149 gold
- SOCKS5: 221 alive / 148 gold

## Historical pool

- Discovered: 127339
- Ever alive: 19762
- Ever gold: 777

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
