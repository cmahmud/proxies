# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 377
- HTTP: 109 alive / 47 gold
- HTTPS: 54 alive / 9 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 182 alive / 163 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33540
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
